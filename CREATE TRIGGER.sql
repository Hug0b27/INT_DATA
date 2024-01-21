CREATE TRIGGER integrationdonnees
ON COMMUNES
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE COMMUNES
    SET integrationladonnees = SYSTEM_USER,
        date_integration = GETDATE()
    FROM COMMUNES
    INNER JOIN INSERTED ON COMMUNES.Code_commune_INSEE = INSERTED.Code_commune_INSEE;
END;

GO
