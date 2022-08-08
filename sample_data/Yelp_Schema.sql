-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Business" (
    "BusinessID" VarChar(25) NOT NULL,
    "BusinessName" VarChar(25) NOT NULL,
    "Address" Text NOT NULL,
    "City" VarChar(25)   NOT NULL,
    "PostalCd" VarChar(10)  NOT NULL,
    "latitude" float   NOT NULL,
    "longitude" float   NOT NULL,
    "StarRating" float   NOT NULL,
    "NumReviews" int   NOT NULL,
    "Close-Open" int   NOT NULL,
    "Attributes" text   NOT NULL,
    "Categories" text   NOT NULL,
    CONSTRAINT "pk_Business" PRIMARY KEY (
        "BusinessID"
     )
);

CREATE TABLE "Reviews" (
    "ReviewID" VarChar(25)   NOT NULL,
    "UserID" VarChar(25)   NOT NULL,
    "BusinessID" VarChar(25)   NOT NULL,
    "Rating" int   NOT NULL,
    "ReviewDate" date   NOT NULL,
    "ReviewTxt" text   NOT NULL,
    CONSTRAINT "pk_Reviews" PRIMARY KEY (
        "ReviewID"
     )
);

CREATE TABLE "User" (
    "UserID" VarChar(25)   NOT NULL,
    "Name" VarChar(25)   NOT NULL,
    "ReviewCount" int   NOT NULL,
    "YelpingSince" date   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "UserID"
     )
);

CREATE TABLE "Tip" (
    "BusinessID" VarChar(25)   NOT NULL,
    "UserID" VarChar(25)   NOT NULL,
    "TipTxt" text   NOT NULL,
    "TipDt" date   NOT NULL
);

ALTER TABLE "Business" ADD CONSTRAINT "fk_Business_BusinessID" FOREIGN KEY("BusinessID")
REFERENCES "Reviews" ("BusinessID");

ALTER TABLE "User" ADD CONSTRAINT "fk_User_UserID" FOREIGN KEY("UserID")
REFERENCES "Reviews" ("UserID");

ALTER TABLE "Tip" ADD CONSTRAINT "fk_Tip_BusinessID" FOREIGN KEY("BusinessID")
REFERENCES "Business" ("BusinessID");

ALTER TABLE "Tip" ADD CONSTRAINT "fk_Tip_UserID" FOREIGN KEY("UserID")
REFERENCES "User" ("UserID");

CREATE INDEX "idx_Business_BusinessName"
ON "Business" ("BusinessName");

