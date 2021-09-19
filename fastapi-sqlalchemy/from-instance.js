import http from "k6/http";
import { check } from "k6";

export let options = {
  stages: [
    {
      duration: "5s",
      target: 1
    },
    {
      duration: "10s",
      target: 1
    }
  ]
};

export default function() {
  const payload = JSON.stringify({
    query: `query {
      allPeople {
        id
        name
      }
    }
    `
  });
  const params = {
    headers: {
      "Content-Type": "application/json"
    }
  };
  const url = "http://localhost:8000";
  const response = http.post(`${url}/graphql/`, payload, params);

  check(response, {
    "is status 200": r => r.status === 200
  });
  check(response, {
    "is response correct": r => {
      return (
        response.json().data.allPeople.length === 10000
      );
    }
  });
}
