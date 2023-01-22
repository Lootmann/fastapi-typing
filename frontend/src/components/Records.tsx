import React from "react";
import axios from "axios";

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

export function Records() {
  const [records, setRecords] = React.useState(null);

  return (
    <div className="text-2xl border-2 border-slate-300 rounded-md p-2">
      <button className="button" onClick={() => getRecords(setRecords)}>
        Get Records
      </button>

      <p>{records}</p>
    </div>
  );
}
