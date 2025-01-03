# Sample plugin for ofxstatement

This project provides a boilerplate for custom plugins for ofxstatement.

[ofxstatement](https://github.com/kedder/ofxstatement) is a tool to convert
proprietary bank statement to OFX format, suitable for importing to GnuCash.
Plugin for ofxstatement parses a particular proprietary bank statement format
and produces common data structure, that is then formatted into an OFX file.

Users of ofxstatement have developed several plugins for their banks. They are
listed on main [ofxstatement](https://github.com/kedder/ofxstatement) site. If
your bank is missing, you can develop your own plugin.

## Usage
For instructions on how to use this plugin to convert your Handelsbanken statements, see [User Guide](USAGE.md).

## Setting up development environment

It is recommended to use `pipenv` to make a clean development environment.
Setting up dev environment for writing a plugin is easy:

```bash
git clone https://github.com/kedder/ofxstatement-sample ofxstatement-yourbank
cd ofxstatement-yourbank
pipenv sync --dev
pipenv shell
```

This will download all the dependencies and install them into your virtual
environment. After this, you should be able to do:

```bash
ofxstatement list-plugins
```

Which will show:

```
The following plugins are available:
  sample           Sample plugin (for developers only)
```

## Your own plugin

To create your own plugin, follow these steps:

- Edit `pyproject.toml` and provide relevant metadata for your plugin. Pay close
  attention to `project.entry-points` section: it lists plugins you are
  registering within ofxstatement. Give meaningful name to the plugin and
  reference your plugin class name.
- Replace contents of `README.md` with description of your plugin
- Rename the project name (`ofxstatement_sample`) to match plugin package name
  you have provided in `entry_points` parameter.
- Open the `plugin.py` and rename `SamplePlugin` and `SampleParser` classes to
  match your plugin class name.
- Now, draw the rest of the owl (c).

Your `StatementParser` is the main object that does all the hard work. It has
only one public method: `parse()`, that should return
`ofxstatement.statement.Statement` object, filled with data from given input.
The default implementation, however, splits this work into two parts:

- `split_records()` to split the whole file into logical parts, e.g. transaction
  records
- `parse_record()` to extract information from individual record

See `src/ofxstatement/parser.py` for details. If your statement's format looks
like CSV file, you might find `CsvStatementParser` class useful: it simplifies
mapping between CSV columns and `StatementLine` attributes.

`Plugin` interface consists only of `get_parser()` method, that returns
configured StatementParser object for given input filename. Docstrings on Plugin
class is also useful for describing the purpose of your plugin. First line of it
is visible in `ofxstatement list-plugins` output.

## Testing

Test your code as you would do with any other project. To make sure ofxstatement
is still able to load your plugin, run:

```bash
ofxstatement list-plugins
```

You should be able to see your plugin listed.

## After you are done

After your plugin is ready, feel free to open an issue on
[ofxstatement](https://github.com/kedder/ofxstatement) project to include your
plugin in "known plugin list". That would hopefully make life of other clients
of your bank easier.
