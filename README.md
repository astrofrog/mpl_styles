About
=====

A collection of pre-defined matplotlib styles

Using
=====

You can either set a global style for the rest of the script:

    mpl_styles.style('style_name')

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ...

or make use of the context manager to temporarily change the style:

    with mpl_styles.style('style_name'):

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ...

Credits
=======

Package inspired from a discussion with Joao Alves (University of Vienna)

