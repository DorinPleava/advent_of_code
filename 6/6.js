const fs = require("fs");

fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  var buffer = "";

  var startOfMessage = 0;

  var skip = false;

  data.split("").forEach((char, index) => {
    if (skip) {
    } else {
      buffer += char;
      if (buffer.length > 3) {
        var bufferSet = new Set(buffer);

        if (bufferSet.size === 4) {
          console.log("all unique at index", index + 1, "buffer: ", buffer);

          startOfMessage = index + 1;
          skip = true;
        } else {
          // remove last char from buffer
          console.log("not all unique at index", index, "buffer: ", buffer);
          buffer = buffer.slice(1);
          console.log("removed last char from buffer: ", buffer);
        }
      }
    }
  });

  console.log("----startOfMessage: ", startOfMessage);
  data = data.slice(startOfMessage);

  data.split("").forEach((char, index) => {
    buffer += char;
    if (buffer.length > 13) {
      var bufferSet = new Set(buffer);

      if (bufferSet.size === 14) {
        console.log(
          "-----all unique at index",
          index + 1 + startOfMessage,
          "buffer: ",
          buffer
        );

        process.exit(0);
      } else {
        // remove last char from buffer
        console.log("not all unique at index", index, "buffer: ", buffer);
        buffer = buffer.slice(1);
        console.log("removed last char from buffer: ", buffer);
      }
    }
  });
});
