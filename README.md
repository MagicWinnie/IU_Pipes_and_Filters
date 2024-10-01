# CV project implementing Pipes and Filters pattern

## Project demo

It can be viewed on YouTube: <https://youtu.be/Vf79vNG5-Z8>

## Project structure

```txt
.
├── README.md   # file you are reading ;)
├── requirements.txt   # libraries that are needed to run
└── src   # source code lies here
    ├── custom_types.py   # shorter type aliases
    ├── filters   # filters lie here
    │   ├── __init__.py
    │   ├── base.py   # base filter
    │   ├── blur.py   # blur filter inherited from base filter
    │   ├── hsv.py   # hsv filter inherited from base filter
    │   ├── mirror.py   # mirror filter inherited from base filter
    │   └── resize.py   # resize filter inherited from base filter
    └── main.py   # script that starts all the threads and connects them with pipes
```

## Team members

Team 24:

- Gleb Bugaev ([g.bugaev@innopolis.university](mailto:g.bugaev@innopolis.university))
- Nail Minnemullin ([n.minnemullin@innopolis.university](mailto:n.minnemullin@innopolis.university))
- Dmitriy Okoneshnikov ([d.okoneshnikov@innopolis.university](mailto:d.okoneshnikov@innopolis.university))
- Vladislav Bolshakov ([v.bolshakov@innopolis.university](mailto:v.bolshakov@innopolis.university))
