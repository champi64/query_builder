#!/usr/bin/python3

class QueryBuilder:
  def __init__(self, table_name):
    self.table_name = table_name
    self.conditions = []

  def where(self, conditions):
    if type(conditions) is dict:
      for key in conditions:
        self.conditions.append((f'`{key}`', '=', str(conditions[key])))
    elif type(conditions) is list:
      for parts in conditions:
        count = len(parts)
        if count == 2:
          self.conditions.append(f'`{parts[0]}`', '=', parts[1])
        elif count == 3:
          self.conditions.append(f'`{parts[0]}`', parts[1], parts[2])
    return self

  def or_where(self, conditions):
    pass

  def get(self):
    pass

  def to_sql(self):
    return (f'SELECT * FROM {self.table_name}'
            f'{self.translate_conditions()}')

  def translate_conditions(self):
    count = len(self.conditions)
    if count == 0: return ''
    conditions = ' AND '.join([' '.join(parts) for parts in self.conditions])
    return f' WHERE {conditions}'
