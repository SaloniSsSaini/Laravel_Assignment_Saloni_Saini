<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Caller\LoginController;

Route::get('/', [LoginController::class, 'index']);
Route::get('/login', [LoginController::class, 'index'])->name('login');
Route::post('/login', [LoginController::class, 'validateUser']);
Route::get('/login/{driver}/start', [LoginController::class, 'redirectToProvider']);
Route::any('/login/{driver}/callback', [LoginController::class, 'handleProviderCallback']);
Route::any('/logout', [LoginController::class, 'Logout']);

Route::middleware(['auth:web'])->group(function () {
    // protected routes
});

/* 🔽 ADD THIS ROUTE (Task-3) */
Route::get('/html-page', function () {
    return view('html-page.calendar');
});
