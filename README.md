# bus-system

## Installation

These guidelines are for installation on a windows machine.

### Prerequisite

- Install `rustc 1.72.0` (require at least 5GB for the `msvc` compiler): [link](https://www.rust-lang.org/tools/install).
- Install `docker`: [link](https://docs.docker.com/desktop/install/windows-install/).

### Starting the server
- Notes: The set up is still stupid so one step missing will cause the server to behave incorrectly.
- Start the `mongo` database with `docker compose up` on the top-level folder.
- Load the data into `mongo` database with `docker exec -it bus-system-db "/tmp/mongo_import.sh"`
- Start the server with `cd backend && cargo run`.

## Team Members

| Name                 | Description    | ID |
| -------------------- | -------------- |----|
| Nguyễn Ngọc Vĩnh     | Title          |18691|
| Phan Chí Thọ         | Text           ||
| Lê Hoàng Đăng Nguyên | defenestration |17028|
| Lê Hoàng Kim Thanh | Front end ||
|                    |||


## Project Descriptions

Build a project to predict the bus congestion
