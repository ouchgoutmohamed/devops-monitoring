FROM loadimpact/k6:latest

COPY multi-endpoint-test.js /load-test.js

ENTRYPOINT ["k6", "run", "/load-test.js"]