--SELECT "Meeting Title Link" FROM meeting_search WHERE "Meeting Title Link" LIKE '/slaa/%';
--SELECT "Meeting Title Link" FROM meeting_search WHERE "Meeting Title Link" LIKE '/alanon/%';
--SELECT "Meeting Title Link" FROM meeting_search WHERE "Meeting Title Link" LIKE '/ga/Long%';
--SELECT * FROM meeting_search WHERE "Meeting Title Link" = '/oa//81760';

SELECT substr("Phone", 1, 3) AS 'Area Code', count(*)
FROM meeting_info WHERE PHONE != '' GROUP BY "Area Code" ORDER BY count(*);
