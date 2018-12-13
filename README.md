# SleekMonkey 1.0.0

A faced paced Monkey Patch for SleekXMPP to better handle TLS certificate date.

## Getting started.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This module is designed to work with `Python >=3.5`.  `Python 2` may work, your milage may very.  The only other requirment is SleekXMPP 1.3.3.  This author assums the user posses a working knowldge of Python and the tools available in the user's choosen envirnment.

The `requirments.txt` file contains a listing of the required Python Modules.  These can be installed using `pip` with the `-r` option.

```
python >=  3.5
$ pip install -r requirements.txt
```

### Getting Started

To use this Monkey patch, first import sleekxmpp then add the following code before you make use of SleekXMPP. 

```
import sleekxmpp
...
try:
    import sleekmonkey
    sleekmonkey.monkey_patch()
except ImportError:
    pass # Assume the fine folks at SleekXMPP have updated as approriate.

```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/porcej/cc71497a2b455f27bca8c879731e68dc) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/porcej/sleekmonkey/tags). 

## Authors

* **Joseph Porcelli** - *Initial work* - [porcej](https://github.com/porcej)

See also the list of [contributors](https://github.com/porcej/sleekmonkey/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

