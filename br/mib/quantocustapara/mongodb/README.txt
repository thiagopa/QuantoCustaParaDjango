Fazer o import para cada arquivo .js, Exemplo :

http://docs.mongodb.org/manual/reference/mongoimport/

 mongoimport -d quantocustapara -c cloud_tag --file cloud_tag.js --stopOnError

http://docs.mongodb.org/manual/reference/mongoexport/

 mongoexport -d quantocustapara -c cloud_tag -o cloud_tag.js --journal
