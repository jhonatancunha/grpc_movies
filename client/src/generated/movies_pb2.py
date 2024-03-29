# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movies.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='movies.proto',
  package='mongomovies',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmovies.proto\x12\x0bmongomovies\"\x15\n\x05Genre\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x15\n\x04\x43\x61st\x12\r\n\x05\x61\x63tor\x18\x01 \x01(\t\"\x18\n\x08Language\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x08\x44irector\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x16\n\x06Writer\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x17\n\x07\x43ountry\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb9\x03\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04plot\x18\x02 \x01(\t\x12\"\n\x06genres\x18\x03 \x03(\x0b\x32\x12.mongomovies.Genre\x12\x0f\n\x07runtime\x18\x04 \x01(\x05\x12\r\n\x05rated\x18\x05 \x01(\t\x12\x1f\n\x04\x63\x61st\x18\x06 \x03(\x0b\x32\x11.mongomovies.Cast\x12\x1a\n\x12num_mflix_comments\x18\x07 \x01(\x05\x12\x0e\n\x06poster\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x10\n\x08\x66ullplot\x18\n \x01(\t\x12(\n\tlanguages\x18\x0b \x03(\x0b\x32\x15.mongomovies.Language\x12\x10\n\x08released\x18\x0c \x01(\t\x12(\n\tdirectors\x18\r \x03(\x0b\x32\x15.mongomovies.Director\x12$\n\x07writers\x18\x0e \x03(\x0b\x32\x13.mongomovies.Writer\x12\x13\n\x0blastupdated\x18\x0f \x01(\t\x12\x0c\n\x04year\x18\x10 \x01(\t\x12\'\n\tcountries\x18\x11 \x03(\x0b\x32\x14.mongomovies.Country\x12\x0c\n\x04type\x18\x12 \x01(\t\":\n\x07Request\x12!\n\x05movie\x18\x02 \x01(\x0b\x32\x12.mongomovies.Movie\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"O\n\x08Response\x12\x0e\n\x06sucess\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\"\n\x06movies\x18\x04 \x03(\x0b\x32\x12.mongomovies.Movie2\xcc\x03\n\x0bMongoMovies\x12>\n\rgetMoviesById\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12<\n\x0b\x64\x65leteMovie\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12=\n\x0cgetAllMovies\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12<\n\x0b\x63reateMovie\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12<\n\x0bupdateMovie\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12\x41\n\x10getMoviesByGenre\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x12\x41\n\x10getMoviesByActor\x12\x14.mongomovies.Request\x1a\x15.mongomovies.Response\"\x00\x62\x06proto3'
)




_GENRE = _descriptor.Descriptor(
  name='Genre',
  full_name='mongomovies.Genre',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mongomovies.Genre.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=50,
)


_CAST = _descriptor.Descriptor(
  name='Cast',
  full_name='mongomovies.Cast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actor', full_name='mongomovies.Cast.actor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=73,
)


_LANGUAGE = _descriptor.Descriptor(
  name='Language',
  full_name='mongomovies.Language',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mongomovies.Language.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=99,
)


_DIRECTOR = _descriptor.Descriptor(
  name='Director',
  full_name='mongomovies.Director',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mongomovies.Director.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=125,
)


_WRITER = _descriptor.Descriptor(
  name='Writer',
  full_name='mongomovies.Writer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mongomovies.Writer.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=149,
)


_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='mongomovies.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mongomovies.Country.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=174,
)


_MOVIE = _descriptor.Descriptor(
  name='Movie',
  full_name='mongomovies.Movie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mongomovies.Movie.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plot', full_name='mongomovies.Movie.plot', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genres', full_name='mongomovies.Movie.genres', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='mongomovies.Movie.runtime', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rated', full_name='mongomovies.Movie.rated', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cast', full_name='mongomovies.Movie.cast', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_mflix_comments', full_name='mongomovies.Movie.num_mflix_comments', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poster', full_name='mongomovies.Movie.poster', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='mongomovies.Movie.title', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fullplot', full_name='mongomovies.Movie.fullplot', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='languages', full_name='mongomovies.Movie.languages', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='released', full_name='mongomovies.Movie.released', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='directors', full_name='mongomovies.Movie.directors', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='writers', full_name='mongomovies.Movie.writers', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastupdated', full_name='mongomovies.Movie.lastupdated', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='mongomovies.Movie.year', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='countries', full_name='mongomovies.Movie.countries', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='mongomovies.Movie.type', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=618,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='mongomovies.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='movie', full_name='mongomovies.Request.movie', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='mongomovies.Request.data', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=678,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='mongomovies.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sucess', full_name='mongomovies.Response.sucess', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='mongomovies.Response.message', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='mongomovies.Response.movies', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=759,
)

_MOVIE.fields_by_name['genres'].message_type = _GENRE
_MOVIE.fields_by_name['cast'].message_type = _CAST
_MOVIE.fields_by_name['languages'].message_type = _LANGUAGE
_MOVIE.fields_by_name['directors'].message_type = _DIRECTOR
_MOVIE.fields_by_name['writers'].message_type = _WRITER
_MOVIE.fields_by_name['countries'].message_type = _COUNTRY
_REQUEST.fields_by_name['movie'].message_type = _MOVIE
_RESPONSE.fields_by_name['movies'].message_type = _MOVIE
DESCRIPTOR.message_types_by_name['Genre'] = _GENRE
DESCRIPTOR.message_types_by_name['Cast'] = _CAST
DESCRIPTOR.message_types_by_name['Language'] = _LANGUAGE
DESCRIPTOR.message_types_by_name['Director'] = _DIRECTOR
DESCRIPTOR.message_types_by_name['Writer'] = _WRITER
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['Movie'] = _MOVIE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Genre = _reflection.GeneratedProtocolMessageType('Genre', (_message.Message,), {
  'DESCRIPTOR' : _GENRE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Genre)
  })
_sym_db.RegisterMessage(Genre)

Cast = _reflection.GeneratedProtocolMessageType('Cast', (_message.Message,), {
  'DESCRIPTOR' : _CAST,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Cast)
  })
_sym_db.RegisterMessage(Cast)

Language = _reflection.GeneratedProtocolMessageType('Language', (_message.Message,), {
  'DESCRIPTOR' : _LANGUAGE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Language)
  })
_sym_db.RegisterMessage(Language)

Director = _reflection.GeneratedProtocolMessageType('Director', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTOR,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Director)
  })
_sym_db.RegisterMessage(Director)

Writer = _reflection.GeneratedProtocolMessageType('Writer', (_message.Message,), {
  'DESCRIPTOR' : _WRITER,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Writer)
  })
_sym_db.RegisterMessage(Writer)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRY,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Country)
  })
_sym_db.RegisterMessage(Country)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Movie)
  })
_sym_db.RegisterMessage(Movie)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:mongomovies.Response)
  })
_sym_db.RegisterMessage(Response)



_MONGOMOVIES = _descriptor.ServiceDescriptor(
  name='MongoMovies',
  full_name='mongomovies.MongoMovies',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=762,
  serialized_end=1222,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMoviesById',
    full_name='mongomovies.MongoMovies.getMoviesById',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteMovie',
    full_name='mongomovies.MongoMovies.deleteMovie',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getAllMovies',
    full_name='mongomovies.MongoMovies.getAllMovies',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='createMovie',
    full_name='mongomovies.MongoMovies.createMovie',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateMovie',
    full_name='mongomovies.MongoMovies.updateMovie',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMoviesByGenre',
    full_name='mongomovies.MongoMovies.getMoviesByGenre',
    index=5,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getMoviesByActor',
    full_name='mongomovies.MongoMovies.getMoviesByActor',
    index=6,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONGOMOVIES)

DESCRIPTOR.services_by_name['MongoMovies'] = _MONGOMOVIES

# @@protoc_insertion_point(module_scope)
