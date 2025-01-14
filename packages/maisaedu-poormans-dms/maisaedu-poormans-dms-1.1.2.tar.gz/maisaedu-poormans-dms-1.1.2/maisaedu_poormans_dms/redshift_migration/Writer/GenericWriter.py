class GenericWriter:
    def __init__(self, env, struct, migrator_redshift_connector):
        self.env = env
        self.struct = struct
        self.migrator_redshift_connector = migrator_redshift_connector

    def set_temp_target_relation(self):
        self.temp_target_relation = (
            f'"temp_{self.struct.target_schema}_{self.struct.target_table}"'
        )

    def set_target_relation(self):
        self.target_relation = (
            f'"{self.struct.target_schema}"."{self.struct.target_table}"'
        )

    def create_table_temp_target_relation(self):
        self.target_cursor.execute(
            f"""
                CREATE TEMP TABLE {self.temp_target_relation} (LIKE {self.target_relation});
            """
        )

    def copy_data_to_target(self, url, target):
        self.target_cursor.execute(
            f"""
                COPY {target}
                FROM '{url}'
                IAM_ROLE '{self.migrator_redshift_connector.iam_role}'
                FORMAT AS CSV
                BLANKSASNULL
                TRUNCATECOLUMNS
                IGNOREHEADER 1
            """
        )

    def insert_data_from_temp_to_target(self):
        self.target_cursor.execute(
            f"""
                INSERT INTO {self.target_relation}
                SELECT * FROM {self.temp_target_relation};
            """
        )

    def delete_upsert_data_from_target(self):
        self.target_cursor.execute(
            f"""
                    DELETE FROM {self.target_relation}
                    USING {self.temp_target_relation}
                    WHERE 1=1
                        {self.create_statement_upsert(self.target_relation, self.temp_target_relation)}
                    ;
                """
        )

    def delete_all_data_from_target(self):
        self.target_cursor.execute(
            f"""
                DELETE FROM {self.target_relation};
            """
        )

    def drop_table_temp_target_relation(self):
        self.target_cursor.execute(
            f"""
                DROP TABLE {self.temp_target_relation};
            """
        )

    def get_serialization_if_has_super(self):
        for c in self.struct.columns:
            if c["target_type"] == "super":
                return "SERIALIZETOJSON"
        return ""

    def create_statement_upsert(self, target_relation, temp_target_relation):
        statement_upsert = ""
        for c in self.struct.columns_upsert:
            statement_upsert = (
                statement_upsert
                + f"""
                    and {target_relation}."{c}" = {temp_target_relation}."{c}" 
                """
            )

        return statement_upsert

    def save_to_redshift(self, operations):
        self.migrator_redshift_connector.connect_target()
        cursor = self.migrator_redshift_connector.target_conn.cursor()

        self.target_cursor = cursor

        self.set_temp_target_relation()
        self.set_target_relation()

        if len(self.struct.columns_upsert) == 0:
            self.is_upsert = False
        else:
            self.is_upsert = True

        self.save_data(operations)

        self.target_cursor.close()
