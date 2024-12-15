const path = require('path');
const gateway = require('express-gateway');
const scheduler = require('./services/queueService/scheduler');

gateway()
  .load(path.join(__dirname, 'config'))
  .run();

scheduler();