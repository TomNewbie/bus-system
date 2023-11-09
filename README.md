# bus-system

## Project Descriptions

Build a project to predict the bus congestion and suggest rerouting.

## Architecture

![Use Case Diagram](/use_case_diagram.png)
![Architecture](/architecture.png)
![Data flow for prediction](https://github.com/TomNewbie/bus-system/assets/84883483/706de93c-f563-4143-9d23-2b4091e04427)

## Doc

[Figma design](https://www.figma.com/file/RnBcweRNbW1IM18LsszHox/Bus-Map?type=design&node-id=0%3A1&mode=design&t=zp1iTHFkQuFmu4Cb-1)

[Jira](https://tho-phan-chi.atlassian.net/jira/software/projects/TG/boards/1)

## Resources

- Data for bus line, bus stop and bus schedule: [GTFS](https://gtfs.de/de/feeds/de_nv/)
- Display map: [Mapbox](https://www.mapbox.com/)

## Team Members

| Name                 | Description | ID    |
| -------------------- | ----------- | ----- |
| Nguyễn Ngọc Vĩnh     | Data        | 18691 |
| Phan Chí Thọ         | Front-end   | 17232 |
| Lê Hoàng Đăng Nguyên | Back-end    | 17028 |
| Lê Hoàng Kim Thanh   | Front-end   | 18047 |
| Trần Quang Minh      | Data        | 17061 |

## Installation

These guidelines are for installation on a windows machine.

### Prerequisite

- Install `rustc 1.72.0` (require at least 5GB for the `msvc` compiler): [link](https://www.rust-lang.org/tools/install).
- Install `docker`: [link](https://docs.docker.com/desktop/install/windows-install/).

### Starting the server

- Notes: The set up is still stupid so one step missing will cause the server to behave incorrectly.
- Start the server with: `docker compose up`
