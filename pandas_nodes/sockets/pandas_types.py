class PandasSeriesSocket(NodeSocket):
    bl_idname = 'NodeSocketPandasSeries'
    bl_label = "Pandas Series"

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

register_class = [PandasSeriesSocket]