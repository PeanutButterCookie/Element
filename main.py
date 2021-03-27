from ElementBackbone import *
import pyglet
import tkinter as tk


# user input
def close_window():
    global Z
    Z = InputField.get()
    root.destroy()


root = tk.Tk()
root.geometry('250x100')
root.title('Element')
root.configure(bg='#FFFFFF')
Label = tk.Label(root, text='Atomic Number', bg='#FFFFFF')
Label.pack()
InputField = tk.Entry(root)
InputField.pack(anchor=tk.CENTER)
B = tk.Button(root, text="Enter", command=close_window, bg='#FFFFFF')
B.pack(anchor=tk.S)
root.mainloop()

if int(Z) in range(1, 119):
    ReqAtom = Element(int(Z))

    ExtraData = ReqAtom.ExtraInfo()  # list of all the extra info
    ReqAtom.Graphs(ReqAtom)  # Generating graphs
    Image = 'energy.png'

    # pyglet window
    ElementWindow = pyglet.window.Window(width=1300, height=700, caption='Element')
    pyglet.gl.glClearColor(255, 255, 255, 255)

    # INFO LABELS

    TextColor = (0, 0, 0, 255)
    TextFont = 'Candara'
    fs = 13

    Symbol = pyglet.text.Label(ExtraData[1][1],
                               font_name='Cambria Math',
                               font_size=90, x=118 if len(ExtraData[1][1]) == 1 else 112,
                               y=410, color=(255, 255, 255, 255),
                               anchor_x='center', anchor_y='center')
    SymbolBorder = pyglet.shapes.Rectangle(x=40, width=150,
                                           y=550, height=150,
                                           color=(0, 0, 0))

    ElementName = pyglet.text.Label(ExtraData[0][0] + ('\t' * 14) + ' -\t\t' + ExtraData[0][1],
                                    font_name=TextFont,
                                    font_size=fs, x=40, y=510,
                                    color=TextColor)

    MassNo = pyglet.text.Label(ExtraData[2][0] + ('\t' * 3) + ' -\t\t' + ExtraData[2][1],
                               font_name=TextFont,
                               font_size=fs, x=40, y=480,
                               color=TextColor)

    Period = pyglet.text.Label(ExtraData[6][0] + ('\t' * 18) + '-\t\t' + ExtraData[6][1],
                               font_name=TextFont,
                               font_size=fs, x=40, y=450,
                               color=TextColor)

    Group = pyglet.text.Label(ExtraData[7][0] + ('\t' * 18) + ' -\t\t' + ExtraData[7][1],
                              font_name=TextFont,
                              font_size=fs, x=40, y=420,
                              color=TextColor)

    Protons = pyglet.text.Label(ExtraData[4][0] + ('\t' * 15) + '-\t\t' + ExtraData[4][1],
                                font_name=TextFont,
                                font_size=fs, x=40, y=390,
                                color=TextColor)

    Neutrons = pyglet.text.Label(ExtraData[3][0] + ('\t' * 11) + ' -\t\t' + ExtraData[3][1],
                                 font_name=TextFont,
                                 font_size=fs, x=40, y=360,
                                 color=TextColor)

    Electrons = pyglet.text.Label(ExtraData[5][0] + ('\t' * 11) + ' -\t\t' + ExtraData[5][1],
                                  font_name=TextFont,
                                  font_size=fs, x=40, y=330,
                                  color=TextColor)

    MeltingPoint = pyglet.text.Label(
        ExtraData[8][0] + ('\t' * 4) + '-\t\t' + ExtraData[8][1] + (' K' if ExtraData[8][1] != 'N.A' else ''),
        font_name=TextFont,
        font_size=fs, x=40, y=300,
        color=TextColor)

    BoilingPoint = pyglet.text.Label(
        ExtraData[9][0] + ('\t' * 6) + '-\t\t' + ExtraData[9][1] + (' K' if ExtraData[9][1] != 'N.A' else ''),
        font_name=TextFont,
        font_size=fs, x=40, y=270,
        color=TextColor)

    SpecificHeat = pyglet.text.Label(
        ExtraData[17][0] + ('\t' * 4) + ' -\t\t' + ExtraData[17][1] + (' K' if ExtraData[17][1] != 'N.A' else ''),
        font_name=TextFont,
        font_size=fs, x=40, y=240,
        color=TextColor)

    NumberOfIsotopes = pyglet.text.Label('Isotopes' + ('\t' * 12) + ' -\t\t' + ExtraData[10][1],
                                         font_name=TextFont,
                                         font_size=fs, x=40, y=210,
                                         color=TextColor)

    Radioactive = pyglet.text.Label(ExtraData[14][0] + ('\t' * 6) + ' -\t\t' + ExtraData[14][1].capitalize(),
                                    font_name=TextFont,
                                    font_size=fs, x=40, y=180,
                                    color=TextColor)

    Type = pyglet.text.Label(ExtraData[12][0] + ('\t' * 20) + '-\t\t' + ExtraData[12][1],
                             font_name=TextFont,
                             font_size=fs, x=40, y=150,
                             color=TextColor)

    Classification = pyglet.text.Label(ExtraData[11][0] + ('\t' * 4) + '-\t\t' + ExtraData[11][1],
                                       font_name=TextFont,
                                       font_size=fs, x=40, y=120,
                                       color=TextColor)

    Origin = pyglet.text.Label(ExtraData[13][0] + ('\t' * 17) + '-\t\t' + ExtraData[13][1],
                               font_name=TextFont,
                               font_size=fs, x=40, y=90,
                               color=TextColor)

    Discoverer = pyglet.text.Label(ExtraData[16][0] + ('\t' * 7) + '-\t\t' + ExtraData[16][1],
                                   font_name=TextFont,
                                   font_size=fs, x=40, y=60,
                                   color=TextColor)

    Discovery = pyglet.text.Label(ExtraData[15][0] + ('\t' * 9) + '-\t\t' + ExtraData[15][1],
                                  font_name=TextFont,
                                  font_size=fs, x=40, y=30,
                                  color=TextColor)

    Note = pyglet.text.Label("""Please Note:
    All values and calculations are based on Bohr's Atomic Model. Advances in science have allowed for the development of more accurate models,such as the Vector Atom Model. However, for most purposes, these values are accurate.
    """
                             , multiline=True, width=600,
                             font_name=TextFont, italic=True,
                             bold=True,
                             font_size=10, x=500, y=100,
                             color=(255, 102, 102, 255))

    # NBBorder = pyglet.shapes.Rectangle(500, 30, width=600, height=150,
    #                                    color=(0, 0, 0))
    # GRAPH

    graph = pyglet.resource.image('energy.png')


    # drawing window elements

    @ElementWindow.event
    def on_draw():
        ElementWindow.clear()
        graph.blit(x=450, y=120)
        SymbolBorder.draw()
        Symbol.draw()
        ElementName.draw()
        MassNo.draw()
        Period.draw()
        Group.draw()
        Protons.draw()
        Neutrons.draw()
        Electrons.draw()
        MeltingPoint.draw()
        BoilingPoint.draw()
        SpecificHeat.draw()
        NumberOfIsotopes.draw()
        Radioactive.draw()
        Type.draw()
        Classification.draw()
        Origin.draw()
        Discoverer.draw()
        Discovery.draw()
        Note.draw()


    pyglet.app.run()

else:
    DumDumWindow = pyglet.window.Window(width=1080, height=608, caption="Atomic numbers~~~")
    PTable = pyglet.resource.image('PTable.png')

    @DumDumWindow.event
    def on_draw():
        PTable.blit(x=0, y=0)


    pyglet.app.run()
