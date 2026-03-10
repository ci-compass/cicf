
Create a DO bucket `cicf-2026`. Then take the creditdntials and set up the .env record:

	$ cp .env-template .env
	# edit .env to be correct

	$ populate-records.py gravational waves
	$ populate-records.py dark matter
	$ populate-records.py national high magnetic field laboratory
	$ populate-records.py mosquito control
	$ populate-records.py south pole
	$ upload_records_s3.py


