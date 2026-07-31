    

def main() -> None:

    example_event = {
        "{task_id0}": {
            "platform": "{cloud_platform}",
            "service": "{cloud_service}"
        },
        "{task_id1}": {
            "platform": "{cloud_platform}",
            "service": "{cloud_service}"
        },
        "{task_id2}": {
            "platform": "{cloud_platform}",
            "service": "{cloud_service}"
        }
    }

    print(example_event.keys())
    for _ in example_event.keys():
        print(_)


if __name__ == '__main__':
    main()
