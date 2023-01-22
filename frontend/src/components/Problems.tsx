import React from "react";
import axios from "axios";

type ProblemType = {
  id: number;
  sentence: string;
};

const url = "http://127.0.0.1:8000/problems";

export function Problems() {
  const [problems, setProblems] = React.useState<ProblemType[]>([]);

  React.useEffect(() => {
    getProblem();
  }, []);

  function getProblem() {
    axios.get(url).then((res) => {
      setProblems(res.data);
    });
  }

  return (
    <div className="text-2xl border-2 border-slate-300 rounded-md p-2">
      <button className="button" onClick={getProblem}>
        Problems
      </button>

      <ul className="problem-list">
        {problems.map((problem) => {
          return <li key={problem.id}>{problem.sentence}</li>;
        })}
      </ul>
    </div>
  );
}
