import yaml


class SQLGenerator:
    def __init__(self, schema_path='conf.yaml'):
        self.schema_path = schema_path

        with open(self.schema_path, 'r') as f:
            self._data = yaml.load(f.read(), Loader=yaml.Loader)

    def generate(self):
        for table_name, data in self._data.items():
            gen_str = f'CREATE TABLE {table_name}({table_name}_id serial PRIMARY KEY, '
            for col_name, col_type in data.get("fields").items():
                gen_str += f'{col_name} {col_type}, '

            gen_str += 'created TIMESTAMP NOT NULL, updated TIMESTAMP);'
            print(gen_str)


if __name__ == '__main__':
    generator = SQLGenerator()
    generator.generate()


