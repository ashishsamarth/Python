from openpyxl.utils import column_index_from_string
# Method to add user provided prefix to value in a given column
# Arguments to this method are:- Row number for header row, Column name & User provided prefix value
def add_suffix_to_cell_val(self, _header_row_num, _col_name, _suffix_val):
    # Fetch the column index from column name using 'ref_col_name_letter_map' method
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # Enumerate over the values from 'get_specific_col_val_by_col_name_in_active_ws' method
    # start with index of (header_row+1) since we need to add prefix values to column values only not column header
    # This updated index start value is used for the row for enumeration
    for _idx, _val in enumerate(self.get_specific_col_val_by_col_name_in_active_ws(_header_row_num, _col_name),
                                start=_header_row_num + 1):
        # LHS: Assign values to each cell in the column
        # RHS: Concatenate existing value of the cell with the prefixed value
        self.my_base_active_ws.cell(row=_idx, column=_col_idx).value = (
                str(self.my_base_active_ws.cell(row=_idx, column=_col_idx).value) + str(_suffix_val))
    # Save workbook
    self.save_wb()
