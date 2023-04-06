import { useState, useEffect } from 'react'
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function App() {
  const [ input, setInput ] = useState('');
  const [data, setData] = useState(null);

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleDelete = async(e) => {
    e.preventDefault();
    axios.delete(`/delete/${e.target.dataset.id}/`)
      .then(() => fetchData());
  };

  const postData = (boi_name) => {
    const data = {
      name: boi_name
    };
    axios.post('/api/', data)
      .then(() => fetchData());
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    postData(input);
    setInput('');
  };
  
  const fetchData = async () => {
    const response = await axios.get('/api/');
    console.log(`response: ${response}`)
    const data = response.data;
    console.log(`response data: ${data}`)
    setData(data)
  };

  useEffect(() => {
    fetchData()
  }, []);

  return (
    <div>
      <h1>COMPREHENSIVE LIST OF BOIS</h1>
      <p>ADD A BOI TO THE LIST</p>
      <form onSubmit={handleSubmit}>
        <input 
          type="text"
          value={input}
          onChange={handleInputChange}/>
        <button>SUBMIT</button>
      </form>
      <h1>BOI LIST</h1>
      {
        data ? [...data].reverse().map((data, index) => {
          return (
            <div key={index}>
              <h2>{data.name}</h2>
              <button data-id={data.id} onClick={handleDelete}>DELETE</button>
            </div>
          )
        }) : <h2>NO BOIS AVAILABLE</h2>
      }
    </div>
  );
}

export default App;
