# TASK1
## _Python Code that receives a country name and it returns the following data:_



- Country’s Full Name
- Country’s Capital
- Country’s Common Language
- Country’s Currency Name
- Country’s Currency rate (Base currency is EURO)

### Note: 
- ###### if you send country that does not exist or not a fullname the server will print "Error" 

## Files:
| File name | Descrition |
| ------ | ------ |
| Dockerfile | contains the docker commands |
| requirements.txt | contains all the external packages |
| task1.py | contains the Python app |
| docker-compose.yml |  |


## Build & Run
make sure that you are in the folder dirctory.
```sh
docker build -t <ImageName> . 
docker run -it -d -p 5000:5000 <ImageName>
```

#### Or :

```sh
docker-compose up -d
```

## Testing 
```sh
curl 'localhost:5000/?name=<CountryName>'
```
for example: 
```sh
curl 'localhost:5000/?name=Italy'
```

## API: 
Country information:

https://restcountries.eu/rest/v2/name/<country_name>?fullText=true

Example:

https://restcountries.eu/rest/v2/name/aruba?fullText=true

Currency information:

http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=ils


