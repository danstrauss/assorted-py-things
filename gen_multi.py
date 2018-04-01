"""
# gen_multi
# A basic constructor for a multi line matrix/list-of-lists.
# Use by calling as:
#     var = gen_multi(number_of_lines_and_columns)
#
# creates a [ ] for X lines by X columns to use it to fill with 
"""
def gen_multi(lines_cols):
  g = {}
  for i in range(0,lines_cols):
    g[i] = {}
    for l in range(0,lines_cols):
      g[i][l] = {}
  return g

# test it out 
# g = gen_multi(51)
# print g
