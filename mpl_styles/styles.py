# TODO: add helper to check font exists and give instructions if not

def style_test():

    import brewer2mpl

    par = {}
    par['axes.color_cycle'] = brewer2mpl.get_map('Set2', 'Qualitative', 7).mpl_colors
    par['font.family'] = 'Georgia'
    par['axes.labelsize'] = 'large'

    return par


def style_white_on_black():

    import brewer2mpl

    par = {}
    par['figure.facecolor'] = 'black'
    par['figure.edgecolor'] = 'none'
    par['axes.facecolor'] = 'black'
    par['axes.edgecolor'] = 'white'
    par['axes.labelcolor'] = 'white'
    par['axes.color_cycle'] = brewer2mpl.get_map('Pastel2', 'Qualitative', 7).mpl_colors
    par['font.family'] = 'Georgia'
    par['axes.labelsize'] = 'large'
    par['grid.color'] = 'white'
    par['patch.edgecolor'] = 'white'
    par['xtick.color'] = 'white'
    par['xtick.labelcolor'] = 'white'
    par['ytick.color'] = 'white'
    par['ytick.labelcolor'] = 'white'
    par['savefig.facecolor'] = 'black'
    par['savefig.edgecolor'] = 'black'

    return par
