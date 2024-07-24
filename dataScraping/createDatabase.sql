-- Create allData table
CREATE TABLE allData (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    location VARCHAR(100) NOT NULL,
    company VARCHAR(100) NOT NULL,
    description NTEXT,
    datePosted BIGINT NOT NULL,
    dateUpdated BIGINT NOT NULL,
    myStatus VARCHAR(50),
    decisionTime BIGINT
);

-- Create myQueue table
CREATE TABLE myQueue (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    timeOfArrival BIGINT NOT NULL,
    FOREIGN KEY (id) REFERENCES allData(id)
);

-- -- Create resumeList table
-- CREATE TABLE resumeList (
--     resumeId INT PRIMARY KEY IDENTITY(1,1),
--     resumeName VARCHAR(255) NOT NULL
-- );

-- Create applyQueue table
CREATE TABLE applyQueue (
    id VARCHAR(36) PRIMARY KEY,
    timeOfArrival BIGINT NOT NULL,
    selectedResume INT,
    FOREIGN KEY (id) REFERENCES allData(id),
    FOREIGN KEY (selectedResume) REFERENCES resumeList(resumeId)
);
