const axios = require('axios');

const scheduleParsing = () => {
  const process = async () => {
    try {
      await axios.get('http://localhost:8080/parse?site=interfax');
    } catch(e) {
      console.error(e)
      return;
    }

    const parsedData = await axios.get('http://localhost:8080/get_latest_news').then(resp => resp.data.data);

    try {
      await axios.post('http://localhost:8080/generate-content', parsedData);
    } catch (e) {
      console.log(e)
    }
  }
  
  process();

  setInterval(async () => {
    process();
  }, 60 * 60 * 1000);
};

module.exports = scheduleParsing;