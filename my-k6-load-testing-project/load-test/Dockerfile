FROM loadimpact/k6:latest

COPY load-test.js /load-test.js

ENTRYPOINT ["k6", "run", "/load-test.js"]