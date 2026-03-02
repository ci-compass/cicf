
# need old version that can create access tokens via the UI
MINIO_VERSION=RELEASE.2025-03-12T18-04-18Z

all: test

test:
	pytest test.py

minio-docker:
	mkdir -p data
	docker run -d -p 9000:9000 -p 9001:9001 \
		-v $(pwd)/data:/data \
		-e "MINIO_ROOT_USER=cicf" \
		-e "MINIO_ROOT_PASSWORD=cicf1234" \
		minio/minio:${MINIO_VERSION} server /data --console-address ":9001"

