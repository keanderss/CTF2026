import type { APIRoute } from "astro";
import jwt from "jsonwebtoken";
import logger from "../lib/logging";

export const prerender = false;

const PASSWORD = import.meta.env.PASSWORD
const JWT_SECRET = import.meta.env.SECRET_JWT_KEY

export const POST: APIRoute = async ({ request, cookies }) => {
  const { password } = await request.json();

  if (password.toLowerCase() !== PASSWORD) {
    logger(`User INCORRECT secret input: ${password}`);
    return new Response("Unauthorized", {
      status: 401,
    });
  }

  logger(`User CORRECT secret input: ${password}`);

  const token = jwt.sign(
    { authenticated: true },
    JWT_SECRET,
    { expiresIn: "30d" }
  );

  cookies.set("auth_token", token, {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
    path: "/",
    maxAge: 60 * 60 * 24 * 30,
  });

  return new Response("Authenticated", {
    status: 200,
  });
};