# PSBS

The PuzzleScript Build System!

PSBS combines multiple files into one puzzlescript source file and can export it to an HTML file or an online game hosted on a gist!

For more information view the [official PSBS Documentation](https://jcmiller11.github.io/PSBS/)

![Screenshot of PSBS in action](https://github.com/jcmiller11/psbs/blob/master/docs/media/screenshot.png?raw=true)

## Features

 - Compile PuzzleScript games from many files using Jinja2 templates!
 - Import images and spritesheets directly into your PuzzleScript game!
 - Load existing PuzzleScript projects right from their gists!
 - Load existing PuzzleScript projects from a source text file!
 - Export PuzzleScript projects to html files!
 - Export PuzzleScript projects to gists!
 - Launch your project from play.html or the PuzzleScript editor!
 - Supports most PuzzleScript forks!
 - Use your favorite version control for your PuzzleScript projects!
 - [Tiled](https://www.mapeditor.org/) level editor integration!
 - Extensible with your own custom Python extensions!

## Installing

If you already have Python 3.8 or greater and pip installed simply run the following command from your terminal

`pip install psbs`

If you don't have Python and pip installed: [Download Python](https://www.python.org/downloads/)

If you already have an older version of PSBS installed you can upgrade to the latest version with

`pip install psbs --upgrade`

## Contributing

While I'd be grateful to receive pull requests, at this moment in time prior to doing an official 1.0.0 release what I would really like help with is testing!  Please use PSBS to its fullest and if you encounter any odd behaviors don't hesitate to raise an Issue!

I would like PSBS to have friendly error handling that returns nice, brief, and useful error messages rather than a full stack trace, however it's challenging to make sure I've caught every possible exception, so if you run into a stack trace while using PSBS please raise an Issue!
