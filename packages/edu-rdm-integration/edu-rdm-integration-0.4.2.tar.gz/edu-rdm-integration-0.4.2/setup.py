from codecs import (
    open,
)
from pathlib import (
    Path,
)

import pip
from packaging.version import (
    Version,
)
from setuptools import (
    find_packages,
    setup,
)


PROJECT = 'edu_rdm_integration'

VERSION = '0.4.2'

current_dir_path = Path().resolve()


#  Получение полного описания
with open(str(current_dir_path / 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(str(current_dir_path / 'CHANGELOG.md'), encoding='utf-8') as f:
    long_description += f.read()


production_requirements_path = current_dir_path / 'requirements' / 'production.txt'


if hasattr(pip, '__version__') and Version(str(pip.__version__)) >= Version('20'):
    from pip._internal.network.session import (
        PipSession,
    )
    from pip._internal.req import (
        parse_requirements,
    )

    requirements = parse_requirements(str(production_requirements_path), session=PipSession())
elif (
    hasattr(pip, '__version__')
    and Version('10.0.0') <= Version(str(pip.__version__)) <= Version('19.3.1')
):
    from pip._internal import (
        download,
        req,
    )

    requirements = req.parse_requirements(str(production_requirements_path), session=download.PipSession())
elif hasattr(pip, '__version__') and Version(str(pip.__version__)) >= Version('7.0'):
    requirements = pip.req.parse_requirements(str(production_requirements_path), session=pip.download.PipSession())
else:
    requirements = pip.req.parse_requirements(str(production_requirements_path))

install_requires = [str(item.requirement) for item in requirements]

setup(
    name=PROJECT.replace('_', '-'),
    version=VERSION,

    description='Интеграция с Региональной витриной данных',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='BARS Group',
    author_email='bars@bars.group',

    url='',
    download_url='',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],

    platforms=['Any'],

    scripts=[],

    provides=[],

    namespace_packages=[],
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=('tests', 'tests.*')),
    include_package_data=True,

    package_data={
        '': [
            '*.conf',
            '*.tmpl',
            '*.sh',
            'Dockerfile',
            '*.yaml',
        ],
    },

    install_requires=install_requires,

    zip_safe=False,
)
