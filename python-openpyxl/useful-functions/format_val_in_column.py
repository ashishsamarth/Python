from openpyxl.styles import PatternFill, Border, Side, Font, Alignment
from openpyxl.utils import column_index_from_string
# Method to format columns values with user defined, horizontal alignment ant font color
# Arguments to this method are: - Row number of the header row, column name,
# Font color in the cells
def format_val_in_column(self, _header_row_num, _col_name, _h_align, _font_color):
    note = 'Valid Values are:- right, justify, general, centerContinuous, fill, center, left, distributed'
    assert _h_align in ['right', 'justify', 'general', 'centerContinuous', 'fill', 'center', 'left',
                        'distributed'], note
    # Valid values for _h_align are (‘right’, ‘justify’, ‘general’,
    # ‘centerContinuous’, ‘fill’, ‘center’, ‘left’, ‘distributed’)
    # Fetch the column index from column name using 'ref_col_name_letter_map' method
    _col_idx = column_index_from_string(self.ref_col_name_letter_map(_header_row_num)[_col_name])
    # Iterate over the rows in the given column until last row excluding header row
    for _row_idx in range(_header_row_num + 1, self.my_base_active_ws_max_row + 1):
        # Set the value cells for easy style formatting
        # The Excel columns start with 1, however when iterating, the tuples start with index 0
        value_cells = self.my_base_active_ws.cell(row=_row_idx, column=_col_idx)
        # Set value cell alignment
        value_cells.alignment = Alignment(wrap_text=False, vertical='top', horizontal=_h_align)
        # Set value cell border
        value_cells.border = self.thin_border
        # Change the color of the font in cells with user selected color
        value_cells.font = Font(bold=False, size=self.cell_font_size,
                                name=self.cell_font_name,
                                color=self._my_color_map[_font_color])
    self.save_wb()