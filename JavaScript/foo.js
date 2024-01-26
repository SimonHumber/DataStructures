import React, { useEffect, useState } from "react";
import axios from "axios";

const ApiComponent = () => {
  const [data, setData] = useState(null);
  const newWord = "tree";
  const url = "https://wordsapiv1.p.rapidapi.com/words/" + newWord;
  const options = {
    method: "GET",
    headers: {
      "X-RapidAPI-Key": "e7d3d20c19msh9909da35cc85505p1c98c1jsn6c2e7f6dc962",
      "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
    },
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(url, options);
        setData(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
};

export default ApiComponent;
