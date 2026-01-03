const express = require("express");
const { Pool } = require("pg");

const app = express();

const pool = new Pool({
  host: process.env.POSTGRES_HOST || "localhost",
  user: "postgres",
  password: "postgres",
  database: "votes",
  port: 5432
});

app.get("/", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT vote, COUNT(*) FROM votes GROUP BY vote"
    );

    let response = "<h1>Voting Results</h1>";
    result.rows.forEach(row => {
      response += `<p>${row.vote}: ${row.count}</p>`;
    });

    res.send(response);
  } catch (err) {
    res.send("<h1>No votes yet</h1>");
  }
});

app.listen(5001, () => {
  console.log("Result app running on port 5001");
});