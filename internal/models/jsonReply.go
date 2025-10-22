package models

import (
	"encoding/json"
	"log"
	"net/http"
)

type JsonErrorResponse struct {
	Error string `json:"error"`
}
type JsonResponse struct {
	Status string `json:"status"`
}

// Error Response
func RespondWithError(w http.ResponseWriter, code int, msg string) {
	RespondWithJSON(w, code, JsonErrorResponse{
		Error: msg,
	})
}

// Generic JSON response function
func RespondWithJSON(w http.ResponseWriter, statusCode int, response interface{}) {
	w.Header().Set("Content-Type", "applcation/json")
	data, err := json.Marshal(response)
	if err != nil {
		log.Printf("error marshalling json: %s", err)
		w.WriteHeader(500)
		return
	}
	w.WriteHeader(statusCode)
	w.Write(data)
}
