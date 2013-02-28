CREATE TABLE meeting_search (
  "Meeting Title" TEXT NOT NULL,
  "Meeting Title Link" TEXT NOT NULL,
  "Location" TEXT NOT NULL,
  "Location Link" TEXT NOT NULL,
  "Address" TEXT NOT NULL,
  "Day" TEXT NOT NULL,
  "Time" TEXT NOT NULL,
  "Fellowship" TEXT NOT NULL,
  "Search Longitude" FLOAT NOT NULL,
  "Search Latitude" FLOAT NOT NULL,
  "Search Page" INTEGER NOT NULL,
  UNIQUE("Meeting Title Link")
);

CREATE TABLE meeting_info (
  "Url" TEXT NOT NULL,
  "Meeting Description" TEXT NOT NULL,
  "Details" TEXT,
  "Format" TEXT,
  "Language" TEXT,
  "Phone" TEXT,
  FOREIGN KEY ("Url") REFERENCES meeting_search ("Meeting Title Link"),
  UNIQUE("Url")
);

CREATE TABLE location (
  "Url" TEXT NOT NULL,
  "Location Description" TEXT NOT NULL,
  FOREIGN KEY ("Url") REFERENCES meeting_search ("Meeting Title Link"),
  UNIQUE("Url")
);

CREATE VIEW meeting AS
SELECT *
FROM meeting_search
JOIN meeting_info ON "meeting_info"."Url" = "Meeting Title Link"
JOIN location ON "location"."Url" = "Location Link";
