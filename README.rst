Jefit Decryptor
===============

|version| `GitHub Repo`_

This repository contains a small script that can be used to decrypt Jefit database files that have been exported from the Jefit app.

Requirements
------------
- Python 3

Exporting the database
----------------------
Before you can run the script, you need to export the Jefit app database to some location on your PC.
To actually export the data from the Jefit app, go to the Jefit app, open Settings and use the 'Backup data' function.
After exporting the data you will have to find a way to get your data off the phone, I recommend using AirDroid:
|airdroid|

Running the script
------------------
To run the script, follow this example.
For the purposes of this example, the location of the database file will be called :code:`/home/user/jefit.bak`.

.. code:: bash

    pip install -r requirements.txt
    python run_app.py --filepath /home/user/jefit.bak

That's it. The decrypted database can be found in the output folder. The filetype is sqlite3, so to open it you need some program that can open that type of files. For instance SqliteBrowser.

.. |version| image:: https://img.shields.io/badge/calver-2018.08.1-blue.svg
  :alt: CalVer format
.. _`GitHub Repo`: https://github.com/Atheuz/Jefit-Decryptor
.. |airdroid| image:: https://i.imgur.com/qiAaaZ6.png
  :alt: airdroid
