export default {
  languageOptions: {
    ecmaVersion: 12,
    sourceType: "module",
    globals: {
      browser: true,
      es2021: true,
    },
  },
  files: ["**/*.ts", "**/*.tsx"],
  plugins: {
    "@typescript-eslint": (await import("@typescript-eslint/eslint-plugin")).default,
    "prettier": (await import("eslint-plugin-prettier")).default,
  },
  rules: {
    ...(await import("eslint-config-prettier")).default.rules,
    ...(await import("eslint-plugin-prettier")).default.configs.recommended.rules,
    ...(await import("@typescript-eslint/eslint-plugin")).default.configs.recommended.rules,
  },
  languageOptions: {
    parser: (await import("@typescript-eslint/parser")).default,
    ecmaVersion: 12,
    sourceType: "module",
    globals: {
      browser: true,
      es2021: true,
    },
  },
};
