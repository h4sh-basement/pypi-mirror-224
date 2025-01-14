
.. Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

..   http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.

 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.


Package ``apache-airflow-providers-amazon``

Release: ``8.5.1``


Amazon integration (including `Amazon Web Services (AWS) <https://aws.amazon.com/>`__).


Provider package
----------------

This is a provider package for ``amazon`` provider. All classes for this provider package
are in ``airflow.providers.amazon`` python package.

You can find package information and changelog for the provider
in the `documentation <https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.5.1/>`_.


Installation
------------

You can install this package on top of an existing Airflow 2 installation (see ``Requirements`` below
for the minimum Airflow version supported) via
``pip install apache-airflow-providers-amazon``

The package supports the following python versions: 3.8,3.9,3.10,3.11

Requirements
------------

=======================================  ==================
PIP package                              Version required
=======================================  ==================
``apache-airflow``                       ``>=2.4.0``
``apache-airflow-providers-common-sql``  ``>=1.3.1``
``apache-airflow-providers-http``
``boto3``                                ``>=1.24.0``
``asgiref``
``watchtower``                           ``~=2.0.1``
``jsonpath_ng``                          ``>=1.5.3``
``redshift_connector``                   ``>=2.0.888``
``sqlalchemy_redshift``                  ``>=0.8.6``
``mypy-boto3-rds``                       ``>=1.24.0``
``mypy-boto3-redshift-data``             ``>=1.24.0``
``mypy-boto3-appflow``                   ``>=1.28.16``
``asgiref``
``mypy-boto3-s3``                        ``>=1.24.0``
=======================================  ==================

Cross provider package dependencies
-----------------------------------

Those are dependencies that might be needed in order to use all the features of the package.
You need to install the specified provider packages in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

.. code-block:: bash

    pip install apache-airflow-providers-amazon[apache.hive]


======================================================================================================================  ===================
Dependent package                                                                                                       Extra
======================================================================================================================  ===================
`apache-airflow-providers-apache-hive <https://airflow.apache.org/docs/apache-airflow-providers-apache-hive>`_          ``apache.hive``
`apache-airflow-providers-cncf-kubernetes <https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes>`_  ``cncf.kubernetes``
`apache-airflow-providers-common-sql <https://airflow.apache.org/docs/apache-airflow-providers-common-sql>`_            ``common.sql``
`apache-airflow-providers-exasol <https://airflow.apache.org/docs/apache-airflow-providers-exasol>`_                    ``exasol``
`apache-airflow-providers-ftp <https://airflow.apache.org/docs/apache-airflow-providers-ftp>`_                          ``ftp``
`apache-airflow-providers-google <https://airflow.apache.org/docs/apache-airflow-providers-google>`_                    ``google``
`apache-airflow-providers-http <https://airflow.apache.org/docs/apache-airflow-providers-http>`_                        ``http``
`apache-airflow-providers-imap <https://airflow.apache.org/docs/apache-airflow-providers-imap>`_                        ``imap``
`apache-airflow-providers-microsoft-azure <https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure>`_  ``microsoft.azure``
`apache-airflow-providers-mongo <https://airflow.apache.org/docs/apache-airflow-providers-mongo>`_                      ``mongo``
`apache-airflow-providers-openlineage <https://airflow.apache.org/docs/apache-airflow-providers-openlineage>`_          ``openlineage``
`apache-airflow-providers-salesforce <https://airflow.apache.org/docs/apache-airflow-providers-salesforce>`_            ``salesforce``
`apache-airflow-providers-ssh <https://airflow.apache.org/docs/apache-airflow-providers-ssh>`_                          ``ssh``
======================================================================================================================  ===================

The changelog for the provider package can be found in the
`changelog <https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.5.1/changelog.html>`_.