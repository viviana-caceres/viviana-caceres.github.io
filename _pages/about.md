---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
Disclaimer: This personal website is under development.

Hi! I'm Viviana, a second-year Ph.D. student and NSF Graduate Research Fellow at Penn State.

My research focuses on modeling gravitational waveforms, estimating parameters of compact binary mergers, and investigating how dark matter inside neutron stars might leave detectable imprints on gravitational wave signals. I work with the [Physics and Astrophysics to the eXtreme (PAX) group](https://sites.psu.edu/infinity/) at Penn State, working under the guidance of B.S. Sathyaprakash. I'm also a member of the [LIGO Scientific Collaboration](https://ligo.org/) and the [Cosmic Explorer Consortium](https://cosmicexplorer.org/index.html#intro).

I completed my bachelor's degree in Theoretical Physics at the University of Puerto Rico at Mayagüez, with a Curricular Sequence in Applied Mathematics. Upon graduating in 2023, I was honored with the Enrico Fermi Prize, awarded by the Physics Department to its most distinguished graduate. 

Beyond research, I'm passionate about physics outreach. I'm an author for [Astrobites](https://astrobites.org/author/vcaceres/) and have volunteered in many public physics demonstrations. This website is a space to share helpful resources, highlight my work, and spread my love of physics!

Outside of physics, I enjoy watching movies, working out, cooking, and making music. Check out my music on [Instagram](https://www.instagram.com/musicbyviviana/) and [Youtube](https://www.youtube.com/@Vivi-kx8cw)! 


Sobre Mí
======
Hola! Mi nombre es Viviana y soy estudiante de segundo año del doctorado y becaria de investigación de la NSF en Penn State. 

Mi investigación se enfoca en modelar las ondas gravitacionales, aproximar los parámetros de las fusiones de objetos compactos e investigar cómo la materia oscura en dentro de las estrellas de neutrones podría dejar huellas detectables en las señales de ondas gravitacionales. Trabajo con el grupo de [Física y Astrofísica al Extremo (PAX, por sus siglas en inglés)](https://sites.psu.edu/infinity/) en Penn State bajo la supervisión de B.S. Sathyaprakash. También soy miembro de la [colaboración científica de LIGO](https://ligo.org/) y el [consorcio Cosmic Explorer](https://cosmicexplorer.org/index.html#intro).

Obtuve mi bachillerato en Física Teórica en la Universidad de Puerto Rico, Recinto Universitario de Mayagüez (¡Antes, Ahora y Siempre... Colegio!), con una secuencia curricular en Matemáticas Aplicadas. Cuando me gradué en el 2023, recibí el Premio Enrico Fermi, otorgado por el Departamento de Física a su estudiante más destacado.

Además de la investigación, me apasiona la comunicación científica. Soy autora para [Astrobites](https://astrobites.org/author/vcaceres/) y he sido voluntaria en varias demostraciones públicas de física. Esta página es un espacio para compartir recursos útiles, compartir mi trabajo y difundir mi amor por la física. 

Fuera del ámbito académico, disfruto ver películas, hacer ejercicio, cocinar y hacer música. ¡Puedes escuchar mi música en [Instagram](https://www.instagram.com/musicbyviviana/) y en [Youtube](https://www.youtube.com/@Vivi-kx8cw)! :)


Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this template](https://github.com/academicpages/academicpages.github.io) by clicking the "Use this template" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
