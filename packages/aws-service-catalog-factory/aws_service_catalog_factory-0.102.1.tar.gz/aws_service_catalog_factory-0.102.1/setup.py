# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['servicecatalog_factory',
 'servicecatalog_factory.commands',
 'servicecatalog_factory.common',
 'servicecatalog_factory.template_builder',
 'servicecatalog_factory.template_builder.cdk',
 'servicecatalog_factory.template_builder.pipeline',
 'servicecatalog_factory.template_builder.troposphere_contstants',
 'servicecatalog_factory.utilities',
 'servicecatalog_factory.waluigi',
 'servicecatalog_factory.workflow',
 'servicecatalog_factory.workflow.codecommit',
 'servicecatalog_factory.workflow.dependencies',
 'servicecatalog_factory.workflow.generic',
 'servicecatalog_factory.workflow.portfolios']

package_data = \
{'': ['*'],
 'servicecatalog_factory': ['portfolios/*', 'schema/*', 'templates/*']}

install_requires = \
['PyYAML==6.0.1',
 'better-boto==0.43.0',
 'boto3==1.19.2',
 'botocore==1.22.2',
 'certifi==2023.7.22',
 'cfn-flip==1.2.3',
 'charset-normalizer==2.0.7',
 'click==7.0',
 'colorclass==2.2.2',
 'deepmerge==0.3.0',
 'docutils==0.14',
 'idna==2.8',
 'jinja2==3.1.2',
 'jmespath==0.10.0',
 'lockfile==0.12.2',
 'luigi==3.3.0',
 'markupsafe==2.0.1',
 'networkx==2.6.3',
 'orjson==3.8.0',
 'python-daemon==2.1.2',
 'python-dateutil==2.8.2',
 'requests==2.31.0',
 's3transfer==0.5.0',
 'setuptools==65.6.3',
 'six==1.16.0',
 'tenacity==8.2.2',
 'terminaltables==3.1.0',
 'tornado==6.2',
 'troposphere==3.1.0',
 'typing-extensions==3.10.0.2',
 'urllib3==1.26.7',
 'yamale==3.0.8']

entry_points = \
{'console_scripts': ['servicecatalog-factory = servicecatalog_factory.cli:cli']}

setup_kwargs = {
    'name': 'aws-service-catalog-factory',
    'version': '0.102.1',
    'description': 'Making it easier to build ServiceCatalog products',
    'long_description': '# aws-service-catalog-factory\n\n![logo](./docs/logo.png) \n\n## What is it?\nThis is a python3 framework that makes it easier to build multi region AWS Service Catalog portfolios.\n\nWith this framework you define a portfolio in YAML.  For each product version in your portfolio you specify which git \nrepository it is in and the framework will build out AWS CodePipelines for each product version.\n\nThese CodePipelines can run CFN_NAG and Cloudformation_rspec on your templates enabling you to check your templates are \ngood quality that they are functionally correct.\n\n## Getting started\n\nYou can read the [installation how to](https://service-catalog-tools-workshop.com/30-how-tos/10-installation/20-service-catalog-factory.html)\nor you can read through the [every day use](https://service-catalog-tools-workshop.com/30-how-tos/50-every-day-use.html)\nguides.\n\nYou can read the [documentation](https://aws-service-catalog-factory.readthedocs.io/en/latest/) to understand the inner \nworkings. \n\n\n## Going further\n\nThe framework is one of a pair.  The other is [aws-service-catalog-puppet](https://github.com/awslabs/aws-service-catalog-puppet).\nWith Service Catalog Puppet you can provision products into multiple regions of multiple accounts using YAML and you can \nshare portfolios across multiple regions of multiple accounts. \n\n## License\n\nThis library is licensed under the Apache 2.0 License. \n',
    'author': 'Eamonn Faherty',
    'author_email': 'aws-service-catalog-tools@amazon.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://service-catalog-tools-workshop.com/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
