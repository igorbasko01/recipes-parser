run: stop-container start-container
	PYTHONPATH=. python ./recipes_parser/main.py
	docker stop ingredient-phrase-tagger

run-extract:
	PYTHONPATH=. python ./recipes_parser/main.py --extract

run-transform: stop-container start-container
	PYTHONPATH=. python ./recipes_parser/main.py --transform
	docker stop ingredient-phrase-tagger

run-load:
	PYTHONPATH=. python ./recipes_parser/main.py --load

start-container:
	docker pull mtlynch/ingredient-phrase-tagger && \
	docker run -t -d --rm --name ingredient-phrase-tagger mtlynch/ingredient-phrase-tagger && \
	docker cp crf_model/20210326_1724-nyt-ingredients-snapshot-2015-49381ad.crfmodel ingredient-phrase-tagger:/

stop-container:
	docker stop ingredient-phrase-tagger || true
