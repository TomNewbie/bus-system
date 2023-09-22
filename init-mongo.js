db.createUser({
  user: 'sample',
  pwd: 'password',
  roles: [
    {
      role: 'readWrite',
      db: 'sampledb',
    },
  ],
});
db.createCollection('sample');
