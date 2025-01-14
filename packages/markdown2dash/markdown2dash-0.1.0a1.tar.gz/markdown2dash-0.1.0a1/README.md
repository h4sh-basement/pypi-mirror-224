## Markdown-2-Dash

.. toc::
    :min_level: 3

Markdown-2-Dash or m2d is a standalone package forked out of the [official documentation for dash-mantine-components](https://www.dash-mantine-components.com).
Some form of m2d has existed since the inception of the documentation, but I figured more people can make use of this to document their dash
apps or component libraries.

Have a look [here](https://github.com/snehilvj/markdown2dash/tree/main/preview) to see how this README would look after parsing with m2d.

### Installation

```bash
pip install markdown2dash
```

```bash
poetry add markdown2dash
```

### Quickstart

Just parse the contents of your markdown file with m2d parser, and voilà! You have a layout ready.

```python
import dash_mantine_components as dmc
from dash import Dash, html

from markdown2dash import parse

with open("../README.md") as f:
    md = f.read()


def render_toc(self, toc):
    paddings = {3: 0, 5: 40}
    links = [
        html.A(
            dmc.Text(text, color="dimmed", size="sm"),
            href="#" + hid,
            style={
                "textTransform": "capitalize",
                "textDecoration": "none",
                "paddingLeft": paddings[level],
            },
        )
        for level, text, hid in toc
    ]
    heading = dmc.Text("Table of Contents", mb=10, weight=500) if links else None
    return dmc.Stack([heading, *links], spacing=4, mt=20, mb=30)


layout = parse(md, toc_renderer=render_toc)

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    dmc.Container(layout, size="lg", p=20),
    withGlobalStyles=True,
    withNormalizeCSS=True,
    theme={
        "primaryColor": "indigo",
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Table": {"defaultProps": {"striped": True, "withBorder": True}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
        },
    },
)

if __name__ == "__main__":
    app.run(debug=True)
```

There's now styling by default, so you'll have to provide your own css. You can do that in two ways:
1. Wrap your layout in a MantineProvider and use it to style your page
2. Create CSS files. You can get started with the one provided in this repository: [styles.css]()

##### Example App

You can also just run the example app included in this project locally.

```bash
python example/app.py
``` 

### Available tokens and class names

m2d can render following types of tokens:

| Token               | Class Name          |
|---------------------|---------------------|
| Links               | .m2d-link           |
| Paragraph           | .m2d-paragraph      |
| Emphasis            | .m2d-emphasis       |
| Strong              | .m2d-strong         |
| Code Span           | .m2d-code span      |
| Heading             | .m2d-heading        |
| Thematic Break      | .m2d-thematic-break |
| Block Code          | .m2d-block-code     |
| Block Quote         | .m2d-block-quote    |
| List Item           | .m2d-list-item      |
| List                | .m2d-list           |
| Strikethrough       | .m2d-strikethrough  |
| Mark                | .m2d-mark           |
| Table               | .m2d-table          |
| Table Head          | .m2d-table-head     |
| Table Body          | .m2d-table-body     |
| Table Row           | .m2d-table-row      |
| Table Cell          | .m2d-table-cell     |
| Admonition          | .m2d-admonition     |
| Image               | .m2d-image          |
| Executable Block    | .m2d-block-exec     |
| Dash Component Docs | .m2d-kwargs         |
| Table of Contents   | << user defined >>  |

### Special Directives

m2d includes some special directives enabling you to do a lot more than just rendering static markdown into a dash layout. 

##### Executable Block

You can use the `exec` directive to embed the output of a python script as well as its source code. This directive expects that 
you have stored the output layout in the variable called `component`.

```markdown
.. exec::example.component
```

Here's the output if you are viewing this in a dash app:

.. exec::example.component

You can hide the source code using the `code` argument, and the border using `border`.

```markdown
.. exec::markdown2dash.example.component
    :code: false
    :border: false
```

##### Admonition

You can use `admonition` directive to add dmc.Alert components in your page.
Admonition directive uses [DashIconify]() to render icons as well.

```markdown
.. admonition::Alert Title
    :icon: radix-icons:github-logo
    
    This is to show that now you can render alerts directly from the markdown.
```

Here's the output if you are viewing this in a dash app:

.. admonition::Alert Title
    :icon: radix-icons:github-logo

    This is to show that now you can render alerts directly from the markdown.

##### Image

Render images using dmc.Image like this:

```markdown
.. image::https://www.dash-mantine-components.com/assets/superman.jpeg
    :width: 300px
    :height: 300px
```

Here's the output if you are viewing this in a dash app:

.. image::https://www.dash-mantine-components.com/assets/superman.jpeg
    :width: 300px
    :height: 300px

##### Dash Component API Docs

It's very simple to add API docs of your component using m2d. You just have to specify the package and the component.
Let's create one for DashIconify:

```markdown
.. kwargs::DashIconify
    :library: dash_iconify
```

Here's the output if you are viewing this in a dash app:

.. kwargs::DashIconify
    :library: dash_iconify
 
##### Table of Contents

In order to get a table of contents using m2d, you need to pass a renderer functions that accepts inputs in the following way:

```python

# a placeholder for self and a list of [<level>, <title>, <id>]
[
    (4, 'Installation', 'installation'),
    (4, 'Quickstart', 'quickstart'), 
    (5, 'Example App', 'example-app'),
    (4, 'Special Directives', 'special-directives'),
    (5, 'Dash Component API Docs', 'dash-component-api-docs'),
    (5, 'Table of Contents', 'table-of-contents')
]
```

Here's the renderer function used on this page:

```python
def render_toc(self, toc):
    paddings = {4: 0, 5: 40}
    links = [
        html.A(
            dmc.Text(text, color="dimmed", size="sm"),
            href="#" + hid,
            style={
                "textTransform": "capitalize",
                "textDecoration": "none",
                "paddingLeft": paddings[level],
            },
        )
        for level, text, hid in toc
    ]
    heading = dmc.Text("Table of Contents", mb=10, weight=500) if links else None
    return dmc.Stack([heading, *links], spacing=4, mt=20, mb=30)
```

And then you can enable TOC lke this:

```markdown
.. toc::
    :min_level: 3
```
