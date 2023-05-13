// GENERATED CODE -- DO NOT EDIT!
'use strict';
var grpc = require('grpc');
var movies_pb = require('./movies_pb.js');
function serialize_Request(arg) {
    if (!(arg instanceof movies_pb.Request)) {
        throw new Error('Expected argument of type Request');
    }
    return Buffer.from(arg.serializeBinary());
}
function deserialize_Request(buffer_arg) {
    return movies_pb.Request.deserializeBinary(new Uint8Array(buffer_arg));
}
function serialize_Response(arg) {
    if (!(arg instanceof movies_pb.Response)) {
        throw new Error('Expected argument of type Response');
    }
    return Buffer.from(arg.serializeBinary());
}
function deserialize_Response(buffer_arg) {
    return movies_pb.Response.deserializeBinary(new Uint8Array(buffer_arg));
}
// serviço
//
var MongoMoviesService = exports.MongoMoviesService = {
    getMoviesById: {
        path: '/MongoMovies/getMoviesById',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    deleteMovie: {
        path: '/MongoMovies/deleteMovie',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    getAllMovies: {
        path: '/MongoMovies/getAllMovies',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    createMovie: {
        path: '/MongoMovies/createMovie',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    updateMovie: {
        path: '/MongoMovies/updateMovie',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    getMoviesByGenre: {
        path: '/MongoMovies/getMoviesByGenre',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
    getMoviesByActor: {
        path: '/MongoMovies/getMoviesByActor',
        requestStream: false,
        responseStream: false,
        requestType: movies_pb.Request,
        responseType: movies_pb.Response,
        requestSerialize: serialize_Request,
        requestDeserialize: deserialize_Request,
        responseSerialize: serialize_Response,
        responseDeserialize: deserialize_Response,
    },
};
exports.MongoMoviesClient = grpc.makeGenericClientConstructor(MongoMoviesService);
