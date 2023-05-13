"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var dotenv = __importStar(require("dotenv"));
dotenv.config();
var mongodb_1 = require("mongodb");
var createMovieProtobuf_1 = require("./utils/createMovieProtobuf");
var OP = {
    'CREATE': 1,
    'FIND_BY_ID': 2,
    'UPDATE': 3,
    'DELETE': 4,
    'FIND_BY_ACTOR': 5,
    'FIND_BY_CATEGORY': 6,
};
// SERVIDOR MONGO
var uri = process.env.MONGO_URI || '';
var database = process.env.DB_NAME || "sample_mflix";
var table = process.env.COLLECTION_NAME || "movies";
var db;
var collection;
var client = new mongodb_1.MongoClient(uri, {
    serverApi: {
        version: mongodb_1.ServerApiVersion.v1,
        strict: true,
        deprecationErrors: true,
    }
});
function getMovieById(collections, id) {
    return __awaiter(this, void 0, void 0, function () {
        var query, mongoMovie, protoMovie, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    query = { _id: new mongodb_1.ObjectId(id) };
                    return [4 /*yield*/, collections.findOne(query)];
                case 1:
                    mongoMovie = _a.sent();
                    if (!mongoMovie)
                        return [2 /*return*/, null];
                    protoMovie = (0, createMovieProtobuf_1.createMovieProtobuf)(mongoMovie);
                    return [2 /*return*/, protoMovie];
                case 2:
                    error_1 = _a.sent();
                    return [2 /*return*/, null];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function deleteMovie(collections, id) {
    return __awaiter(this, void 0, void 0, function () {
        var query, result, error_2;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    query = { _id: new mongodb_1.ObjectId(id) };
                    return [4 /*yield*/, collections.deleteOne(query)];
                case 1:
                    result = _a.sent();
                    if (!result || !result.deletedCount) {
                        return [2 /*return*/, false];
                    }
                    return [2 /*return*/, true];
                case 2:
                    error_2 = _a.sent();
                    return [2 /*return*/, false];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function getAllMovies(collection) {
    return __awaiter(this, void 0, void 0, function () {
        var moviesMongo, protoMovies, error_3;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    return [4 /*yield*/, collection.find({}).toArray()];
                case 1:
                    moviesMongo = _a.sent();
                    protoMovies = moviesMongo.map(function (item) { return (0, createMovieProtobuf_1.createMovieProtobuf)(item); });
                    return [2 /*return*/, protoMovies];
                case 2:
                    error_3 = _a.sent();
                    return [2 /*return*/, []];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function createMovie(collection, movie) {
    return __awaiter(this, void 0, void 0, function () {
        var jsonMovie, created, error_4;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    jsonMovie = movie.toObject();
                    return [4 /*yield*/, collection.insertOne({
                            plot: jsonMovie.plot,
                            genres: jsonMovie.genresList.map(function (obj) { return obj.name; }),
                            runtime: jsonMovie.runtime,
                            cast: jsonMovie.castList.map(function (obj) { return obj.actor; }),
                            num_mflix_comments: jsonMovie.numMflixComments,
                            title: jsonMovie.title,
                            fullplot: jsonMovie.fullplot,
                            countries: jsonMovie.countriesList.map(function (obj) { return obj.name; }),
                            released: jsonMovie.released,
                            directors: jsonMovie.directorsList.map(function (obj) { return obj.name; }),
                            rated: jsonMovie.rated,
                            lastupdate: jsonMovie.lastupdated,
                            year: jsonMovie.year,
                            type: jsonMovie.type,
                            writers: jsonMovie.writersList.map(function (obj) { return obj.name; }),
                            languages: jsonMovie.languagesList.map(function (obj) { return obj.name; }),
                        })];
                case 1:
                    created = _a.sent();
                    if (!created)
                        return [2 /*return*/, null];
                    return [2 /*return*/, String(created.insertedId)];
                case 2:
                    error_4 = _a.sent();
                    return [2 /*return*/, null];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function getMoviesByGenre(collection, genre) {
    return __awaiter(this, void 0, void 0, function () {
        var value, query, moviesMongo, protoMovies, error_5;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    value = genre.getName();
                    query = { genres: { $elemMatch: { $eq: value } } };
                    return [4 /*yield*/, collection.find(query).toArray()];
                case 1:
                    moviesMongo = _a.sent();
                    protoMovies = moviesMongo.map(function (item) { return (0, createMovieProtobuf_1.createMovieProtobuf)(item); });
                    return [2 /*return*/, protoMovies];
                case 2:
                    error_5 = _a.sent();
                    return [2 /*return*/, []];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function getMoviesByActor(collection, cast) {
    return __awaiter(this, void 0, void 0, function () {
        var actor, query, moviesMongo, protoMovies, error_6;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    actor = cast.getActor();
                    query = { cast: { $elemMatch: { $eq: actor } } };
                    return [4 /*yield*/, collection.find(query).toArray()];
                case 1:
                    moviesMongo = _a.sent();
                    protoMovies = moviesMongo.map(function (item) { return (0, createMovieProtobuf_1.createMovieProtobuf)(item); });
                    return [2 /*return*/, protoMovies];
                case 2:
                    error_6 = _a.sent();
                    return [2 /*return*/, []];
                case 3: return [2 /*return*/];
            }
        });
    });
}
function updateMovie(collection, id, movie) {
    return __awaiter(this, void 0, void 0, function () {
        var jsonMovie, idObject, acknowledged, error_7;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    jsonMovie = movie.toObject();
                    idObject = new mongodb_1.ObjectId(id);
                    return [4 /*yield*/, collection.updateOne({ _id: idObject }, { $set: {
                                plot: jsonMovie.plot,
                                genres: jsonMovie.genresList.map(function (obj) { return obj.name; }),
                                runtime: jsonMovie.runtime,
                                cast: jsonMovie.castList.map(function (obj) { return obj.actor; }),
                                num_mflix_comments: jsonMovie.numMflixComments,
                                title: jsonMovie.title,
                                fullplot: jsonMovie.fullplot,
                                countries: jsonMovie.countriesList.map(function (obj) { return obj.name; }),
                                released: jsonMovie.released,
                                directors: jsonMovie.directorsList.map(function (obj) { return obj.name; }),
                                rated: jsonMovie.rated,
                                lastupdate: jsonMovie.lastupdated,
                                year: jsonMovie.year,
                                type: jsonMovie.type,
                                writers: jsonMovie.writersList.map(function (obj) { return obj.name; }),
                                languages: jsonMovie.languagesList.map(function (obj) { return obj.name; }),
                            } })];
                case 1:
                    acknowledged = (_a.sent()).acknowledged;
                    return [2 /*return*/, acknowledged];
                case 2:
                    error_7 = _a.sent();
                    throw error_7;
                case 3: return [2 /*return*/];
            }
        });
    });
}
var grpc_1 = __importDefault(require("grpc"));
var proto_loader_1 = require("@grpc/proto-loader");
var movies_grpc_pb_1 = require("./generated/movies_grpc_pb");
var packageDefinition = (0, proto_loader_1.loadSync)('src/proto/movies.proto');
var proto = grpc_1.default.loadPackageDefinition(packageDefinition);
console.log('proto', proto);
var MongoMovies = /** @class */ (function (_super) {
    __extends(MongoMovies, _super);
    function MongoMovies() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return MongoMovies;
}(movies_grpc_pb_1.MongoMoviesService));
// await client.connect();
// db = client.db(database);
// collection = db.collection(table);
// class MongoMovies implements MongoMoviesServices {
// }
// const server = new grpc.Server();
// server.addService(MongoMoviesService, new Greeter());
// server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
// server.start();
