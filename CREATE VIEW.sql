CREATE VIEW Vue_Nord_Pas_de_Calais AS
SELECT *
FROM COMMUNES
WHERE LEFT(code_postal, 2) IN ('59', '62');
