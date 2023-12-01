const fs = require("fs");

var crates = {};
var operations = [];
fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  // console.log(data);

  var lines = data.split("\n\n")[0].split("\n");

  operations = data.split("\n\n")[1].split("\n");

  var crates_nr = lines.pop().split("   ").length;
  console.log("crates_nr: ", crates_nr);

  // crates = {};

  for (let i = 0; i < crates_nr; i++) {
    crates[i + 1] = [];
  }

  lines.forEach((line) => {
    console.log("line: ", line);
    line.match(/.{1,4}/g).forEach((crate_value, index) => {
      // console.log("crate_value: ", crate_value,);
      // console.log("crates[index]: ", crates[index]);

      // console.log("adding crate_value: ", crate_value, " to index: ", index);
      if (crate_value.replace(/\s/g, "").length > 0) {
        crates[index + 1].unshift(crate_value);
      }
      // crates[index + 1].push(crate_value);
      // console.log("added crate_value: ", crate_value, " to index: ", index);
      // console.log("crates[index]: ", crates[index]);
    });
  });
  console.log("crates before: ", crates);

  console.log(operations);

  operations.forEach((operation) => {
    var number_of_crates_to_move = parseInt(operation.match(/\d+/g)?.[0]);
    var crates_to_move_from = parseInt(operation.match(/\d+/g)?.[1]);
    var crates_to_move_to = parseInt(operation.match(/\d+/g)?.[2]);

    // console.log("number_of_crates_to_move: ", number_of_crates_to_move);
    // console.log("crates_to_move_from: ", crates_to_move_from);
    // console.log("crates_to_move_to: ", crates_to_move_to);

    console.log(
      "Moving ",
      number_of_crates_to_move,
      " crates from ",
      crates_to_move_from,
      " to ",
      crates_to_move_to
    );

    console.log("-------------------------------");
    
    temporary_crates = [];
    // part 1 
    for (let i = 0; i < parseInt(number_of_crates_to_move); i++) {
      // console.log("crates[crates_to_move_to]: ", crates[crates_to_move_to]);

      var crate_to_move = crates[crates_to_move_from].pop();

      console.log("crate_to_move: ", crate_to_move);
      // crates[crates_to_move_to].push(crates[crates_to_move_from].shift());

      // crates[crates_to_move_to].push(crate_to_move);

      temporary_crates.push(crate_to_move);
      console.log("crates after: ", crates);
      console.log("-------------------------------");
      // if (crate_to_move.replace(/\s/g, '').length > 0) {
      //   crates[crates_to_move_to].push(crate_to_move);
      // }else{
      //   console.log("crate_to_move is empty");
      // }
    }

    // part 2

    // reverse temportary crates
    temporary_crates.reverse();
    crates[crates_to_move_to].push(...temporary_crates);

  });


  // part 2

  console.log("crates after: ", crates);

// result = "";
  // crates_nr.forEach((crate) => {
  //   result += crate.join("   ");
  // }
  // console.log("result: ", result);

  result = "";

  for (let i = 1; i <= crates_nr; i++) {

    char = crates[i].pop();

    if (char) {
      result += char.replace(/\[|\]|\s/g, "");
    }
  }

  console.log("result: ", result);

});

