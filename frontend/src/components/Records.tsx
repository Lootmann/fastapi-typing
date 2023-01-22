import React from "react";
import axios from "axios";

export function Records() {
  const [records, setRecords] = React.useState(null);

  return (
    <div className="border">
      <button className="button" onClick={() => getRecords(setRecords)}>
        Get Records
      </button>

      <p>{records}</p>
    </div>
  );
}

function getRecords(props: any) {
  const url = "http://127.0.0.1:8000/records";

  axios
    .get(url)
    .then((res) => {
      props.setRecords(res.data);
    })
    .catch((error) => {
      console.log(error);
    });
}
