setInterval(() => {
  console.log(`${new Date().toISOString()}: ${crypto.randomUUID()}`);
}, 5000);
