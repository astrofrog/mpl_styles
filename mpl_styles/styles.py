# TODO: add helper to check font exists and give instructions if not

def style_test():
    import brewer2mpl
    par = {}
    par['axes.color_cycle'] = brewer2mpl.get_map('Set2', 'Qualitative', 7).mpl_colors
    par['font.family'] = 'Georgia'
    par['axes.labelsize'] = 'large'
    return par
